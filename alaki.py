import numpy as np
import sys
import random
import time
import itertools as IT
import logging
import networkx as nx
import pandas as pd
import multiprocessing as mp
import igraph

'''phase 2---------------------------------------------------------------------------------'''
df = pd.read_csv("person.csv")
df = df[(df['work'].str.contains("بندر")) | (df['work'].str.contains('گمرک'))]
dataFrame = pd.read_csv("relationship.csv")
df = df.rename(columns={'ssn': 'from'})
flag_data_frame = pd.merge(df, dataFrame, on=['from'], how='inner')
flag_data_frame = flag_data_frame.drop_duplicates()
dataf = pd.read_csv('ownership.csv')
flag_data_frame1 = flag_data_frame.drop(['to', 'relation', 'date', 'first_name', 'last_name', 'birthday', 'work', 'city'], axis=1)
flag_data_frame1 = pd.merge(flag_data_frame1, dataf, on=['from'], how='inner')
flag_data_frame1 = flag_data_frame1.drop_duplicates()
flag_data_frame1.to_csv('noni.csv', index=False)
# print(flag_data_frame1)
flag_data_frame2 = flag_data_frame.drop(['from', 'relation', 'date', 'first_name', 'last_name', 'birthday', 'work', 'city'], axis=1)
flag_data_frame2 = flag_data_frame2.rename(columns={'to': 'from'})
flag_data_frame2 = pd.merge(flag_data_frame2, dataf, on=['from'], how='inner')
flag_data_frame2 = flag_data_frame2.drop_duplicates()
# print(flag_data_frame2)
flag_data_frame2 = pd.concat([flag_data_frame2, flag_data_frame1], axis=0, sort=False)
flag_data_frame2 = flag_data_frame2.drop_duplicates()
print(flag_data_frame2)
flag_data_frame2.to_csv('noni.csv', index=False)
'''--------------------------------------------------------------------------------------'''
'''phase3--------------------------------------------------------------------------------'''
logger = mp.log_to_stderr(logging.DEBUG)


def worker(inqueue, output):
    result = []
    count = 0
    for pair in iter(inqueue.get, sentinel):
        source, target = pair
        try:
            # r = nx.has_path(tr, source=source, target=target)
            # r = nx.all_simple_paths(tr, source=source, target=target, cutoff=10)
            if nx.has_path(tr, source=source, target=target):
                print(source, target)
                result.append((source, target))
                count += 1
                if count % 10 == 0:
                    logger.info('{c}'.format(c=count))
        except:
            continue
    output.put(result)


def test_workers():
    result = []
    inqueue = mp.Queue()
    for source, target in IT.product(sources, targets):
        inqueue.put((source, target))
    procs = [mp.Process(target=worker, args=(inqueue, output))
             for _ in range(4)]
    for proc in procs:
        proc.daemon = True
        proc.start()
    for proc in procs:
        inqueue.put(sentinel)
    for proc in procs:
        result.extend(output.get())
    for proc in procs:
        proc.join()
    return result


sentinel = None

transaction = pd.read_csv('transaction.csv')
tr = nx.from_pandas_edgelist(transaction, 'from', 'to', create_using=nx.DiGraph())
df = pd.read_csv("person.csv")
employees = df[(df['work'].str.contains("بندر")) | (df['work'].str.contains('گمرک'))]
smugglers = df[df['work'].str.contains('قاچاقچی')]
smugglers = pd.merge(smugglers, pd.read_csv('account.csv'), on=['ssn'], how='inner')
employees = pd.merge(employees, pd.read_csv('account.csv'), on=['ssn'], how='inner')
# employees = np.array(employees['account_id'])
# smugglers = np.array(smugglers['account_id'])
sources = list(smugglers['account_id'])
targets = list(employees['account_id'])
print(len(sources), len(targets))
output = mp.Queue()
s = test_workers()
rel = pd.DataFrame(s, columns=['from', 'to'])
rel.to_csv('reli.csv', index=False)
print("finish")

'''---------------------------------------------------------------------------------------------'''
'''phase4---------------------------------------------------------------------------------------'''
rel = rel.rename(columns={'from': 'account_id'})
f = pd.merge(rel, pd.read_csv('account.csv'), on=['account_id'], how='inner')
f = f.drop(['to', 'account_id', 'bank_name', 'IBAN'], axis=1)
rel = rel.rename(columns={'account_id': 'from'})
rel = rel.rename(columns={'to': 'account_id'})
t = pd.merge(rel, pd.read_csv('account.csv'), on=['account_id'], how='inner')
t = t.drop(['from', 'account_id', 'bank_name', 'IBAN'], axis=1)
f = pd.merge(f, pd.read_csv('phone.csv'), on=['ssn'], how='left')
t = pd.merge(t, pd.read_csv('phone.csv'), on=['ssn'], how='left')
f = f.drop(['ssn', 'operator'], axis=1)
f = f.rename(columns={'number': 'from'})
t = t.drop(['ssn', 'operator'], axis=1)
t = t.rename(columns={'number': 'to'})
concat = pd.concat([f, t], axis=1, sort=False)
concat = concat.dropna()
concat = concat.reset_index(drop=True)
concat = concat.astype(int)
concat = concat.drop_duplicates(subset='to', keep='last')
w = pd.merge(concat, pd.read_csv('contact.csv'), on=['from', 'to'])
concat = concat.rename(columns={'from': 'to', 'to': 'from'})
x = pd.merge(concat, pd.read_csv('contact.csv'), on=['from', 'to'])
x = x[['from', 'to', 'call_id', 'date', 'duration']]
print(x)
# print(concat)
print(w)
z = pd.concat([w, x], axis=0)
print(z)


