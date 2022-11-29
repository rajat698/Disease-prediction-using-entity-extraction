#Function to give a training sample to the trainner
def entitiesSet():
    text = open('diseasedata.txt', 'r').read()
    #Entity tagging
    train = [(text, {"entities": [(654,661, 'DISEASE'),(1890,1896, 'DISEASE'),(2311,2323, 'DISEASE'),
                                              (1382,1391, 'DISEASE'), (406,414, 'DISEASE'), 
                                              (2539,2543, 'DISEASE'), (168,177, 'DISEASE'),
                                            (2325,2327, 'DISEASE'), (518,524, 'DISEASE'),(3028,3038,'DISEASE'),(3101,3110, 'DISEASE'),
                                              (3264,3268, 'DISEASE'), (3360,3364, 'DISEASE'), (3494,3507, 'DISEASE'),
                                              (3600,3612, 'DISEASE'), (3683,3689, 'DISEASE'), (3736,3757, 'DISEASE')
                                              , (3874,3885, 'DISEASE'), (4044,4051, 'DISEASE'), (4145,4184, 'DISEASE'), (4326,4334, 'DISEASE'),
                                              (4450,4462, 'DISEASE'), (4551,4558, 'DISEASE'), (4638,4648, 'DISEASE'),
                                              (4763, 4773, 'DISEASE'), (5613, 5621, 'DISEASE'), (7250, 7258, 'DISEASE'), (8205, 8213, 'DISEASE'), (5405,5414, 'SYMPTOM'), (5512, 5520, 'SYMPTOM'), (6825, 6832, 'SYMPTOM'),
                    (6847, 6856, 'SYMPTOM'), (6910, 6917, 'SYMPTOM'), (7057, 7062, 'SYMPTOM'), (7067, 7071, 'SYMPTOM'),
                    (7195, 7205, 'SYMPTOM'), (8063, 8071, 'SYMPTOM'), (8099, 8103, 'SYMPTOM'), (8134, 8139, 'SYMPTOM'), (8142, 8148, 'SYMPTOM'), (8153, 8161, 'SYMPTOM'), (8422, 8427, 'SYMPTOM'), (8902, 8910, 'SYMPTOM'),
                    (8920, 8925, 'SYMPTOM'), (8928, 8932, 'SYMPTOM'), (9973, 9977, 'SYMPTOM'), (8643, 8654, 'TREATMENT'), (5256, 5265, 'TREATMENT'), (5266, 5275, 'TREATMENT'), (5277, 5283, 'TREATMENT'),
                    (5288, 5296, 'TREATMENT'), (7814, 7824, 'TREATMENT'), (10576, 10585, 'TREATMENT'), (10354, 10364, 'DISEASE'), (10601, 10614, 'DISEASE'), (10863, 10874, 'TREATMENT'), (10876, 10886, 'TREATMENT')
                    , (10887, 10898, 'TREATMENT'), (10918, 10925, 'TREATMENT'), (11353, 11366, 'DISEASE'), (11330, 11337, 'TREATMENT'), (11342, 11351, 'TREATMENT'), (11468, 11479, 'DISEASE'), (11663, 11675, 'TREATMENT')]})]

    return train
