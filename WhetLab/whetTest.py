import whetlab
parameters = { 'C':{'min':0.01, 'max':1000.0,'type':'float'},
               'degree':{'min':1, 'max':5,'type':'integer'}}
outcome = {'name':'Classification accuracy'}
access_token = 'b8988953-d6ec-46f3-a97e-5ced93f5a642'
scientist = whetlab.Experiment(name="Web page classifier",
                               description="Training a polynomial kernel SVM to classify web pages.",
                               parameters=parameters,
                               outcome=outcome,
                               access_token=access_token)

