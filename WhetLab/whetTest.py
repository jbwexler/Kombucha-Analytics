import whetlab

parameters = { 'TeaType'      :{'type':'enum',  'options':['ShouPuer','ShengPuer','GreenOolong','DarkOolong','Green','White']},
               'WaterVol [L]' :{'type':'float', 'min':0, 'max':10},
             }
               
outcome = {'name':'Taste [0-10]'}
access_token = 'b8988953-d6ec-46f3-a97e-5ced93f5a642'

scientist = whetlab.Experiment(name="Kombucha Analytics",
                               description="Using machine learning to make great booch.",
                               parameters=parameters,
                               outcome=outcome,
                               access_token=access_token)

job1 = {u'TeaType': 'ShouPuer','WaverVol [L]': 3.0}
scientist.update(job1, 3.2)
scientist.report()
