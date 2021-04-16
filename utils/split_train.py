import json

PRED_FILE_PATH = '../model_gtt/preds_gtt.out'
PRED_DIRECTORY_PATH = '../model_gtt/preds_gtt/'

def main():
  with open(PRED_FILE_PATH, 'r') as r:
    train_examples = json.load(r)
    for key in train_examples:
      data = train_examples[key]
      data['docid'] = key
      with open(PRED_DIRECTORY_PATH + key + '.json', 'w') as w:
        json.dump(data, w)
 
if __name__ == '__main__':
  main()