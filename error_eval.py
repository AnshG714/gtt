import argparse
import json

def analyze_for_listed_field(list_pred, list_gold):

  for gold_values in list_gold:
    match_found = False
    error_recorded = False
    for pred_values in list_pred:
      # remove the integers in the gold file. 
      gold_values_cleaned = []
      for val in gold_values:
        gold_values_cleaned.append(val[0])

      print(pred_values)
      print(gold_values_cleaned)

      if pred_values != [] and pred_values[0] in gold_values_cleaned:
        match_found = True
        break
      
      error_recorded = True
      if pred_values == [] and gold_values_cleaned != []:
        print('potential MISSING_ENTITY, correct gold values', str(gold_values_cleaned))
      else:
        print('potential INCORRECT_ENTITY, \tprediction:', '"' + pred_values[0] + '"', '\tactual list:', str(gold_values_cleaned))

    if error_recorded and match_found:
      print('UNDOing error recording required.')

def analyze(pred_template, gold_template):

  # simple check: the incident field. 
  if pred_template['incident_type'] != gold_template['incident_type']:
    print('Incorrect incident_type. Predicted:', pred_template['incident_type'], 'Actual:', gold_template['incident_type'])

  analyze_for_listed_field(pred_template['PerpInd'], gold_template['PerpInd'])
  
  pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--pred_file', '-p', type=str, required=True, help="preds output file")
  parser.add_argument('--gold_file', '-g', type=str, required=True, help="gold template file")
  
  pred_file_prefix = 'model_gtt/preds_gtt/'
  gold_file_prefix = 'data/muc/processed/test/'
  args = parser.parse_args()

  with open(pred_file_prefix + args.pred_file, encoding="utf-8") as f:
    # only read the first template for now. 
    pred_template = json.load(f)['pred_templates'][0]

  with open(gold_file_prefix + args.gold_file, encoding="utf-8") as f:
    # read first gold template.
    gold_template = json.load(f)['templates'][0]

  analyze(pred_template, gold_template)