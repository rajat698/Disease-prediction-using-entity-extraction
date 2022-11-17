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
                                              (4763, 4773, 'DISEASE'), (5613, 5621, 'DISEASE'), (7250, 7258, 'DISEASE'), (8205, 8213, 'DISEASE'), (5405,5414, 'SYMPTOPM'), (5512, 5520, 'SYMPTOPM'), (6825, 6832, 'SYMPTOPM'),
                    (6847, 6856, 'SYMPTOPM'), (6910, 6917, 'SYMPTOPM'), (7057, 7062, 'SYMPTOPM'), (7067, 7071, 'SYMPTOPM'),
                    (7195, 7205, 'SYMPTOPM'), (8063, 8071, 'SYMPTOPM'), (8099, 8103, 'SYMPTOPM'), (8134, 8139, 'SYMPTOPM'), (8142, 8148, 'SYMPTOPM'), (8153, 8161, 'SYMPTOPM'), (8422, 8427, 'SYMPTOPM'), (8902, 8910, 'SYMPTOPM'),
                    (8920, 8925, 'SYMPTOPM'), (8928, 8932, 'SYMPTOPM'), (9973, 9977, 'SYMPTOPM')]})]

    return train
