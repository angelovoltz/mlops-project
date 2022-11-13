import os
import git
import pandas as pd
from argparse import ArgumentParser

# Exercicio 1
#parser = ArgumentParser()
#parser.add_argument('--arg_1', required=True, type=int)
#parser.add_argument('--arg_2', required=False, type=int)
#args = parser.parse_args()
#print(args.arg_1, args.arg_2)


# Exercicio 2
#parser = ArgumentParser()
#parser.add_argument('--base_data_url', required=True)
#args = parser.parse_args()

#git.Repo.clone_from(args.base_data_url, 'data')


# Exercicio 3
parser = ArgumentParser()
parser.add_argument('--data_file_name', required=True)
args = parser.parse_args()

data = pd.read_csv(os.path.join(os.getcwd(), 'data', args.data_file_name), sep=',', encoding='utf-8')

print(data)