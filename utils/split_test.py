import json

TEST_FILE_PATH = '../data/muc/processed/test.json'
TEST_DIRECTORY_PATH = '../data/muc/processed/test/'

def main():
  with open(TEST_FILE_PATH, 'r') as r:
    for line in r:
      test_example = json.loads(line)
      docid = test_example['docid']
      with open(TEST_DIRECTORY_PATH + docid + '.json', 'w') as w:
        json.dump(test_example, w)

if __name__ == "__main__":
  main()
