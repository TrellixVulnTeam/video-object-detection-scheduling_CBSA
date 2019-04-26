# coco_category_map = {
#     1: 'person',
#     2: 'bicycle',
#     3: 'car',
#     4: 'motorcycle',
#     5: 'airplane',
#     6: 'bus',
#     7: 'train',
#     8: 'truck',
#     9: 'boat',
#     10: 'traffic light',
#     11: 'fire hydrant',
#     13: 'stop sign',
#     14: 'parking meter',
#     15: 'bench',
#     16: 'bird',
#     17: 'cat',
#     18: 'dog',
#     19: 'horse',
#     20: 'sheep',
#     21: 'cow',
#     22: 'elephant',
#     23: 'bear',
#     24: 'zebra',
#     25: 'giraffe',
#     27: 'backpack',
#     28: 'umbrella',
#     31: 'handbag',
#     32: 'tie',
#     33: 'suitcase',
#     34: 'frisbee',
#     35: 'skis',
#     36: 'snowboard',
#     37: 'sports ball',
#     38: 'kite',
#     39: 'baseball bat',
#     40: 'baseball glove',
#     41: 'skateboard',
#     42: 'surfboard',
#     43: 'tennis racket',
#     44: 'bottle',
#     46: 'wine glass',
#     47: 'cup',
#     48: 'fork',
#     49: 'knife',
#     50: 'spoon',
#     51: 'bowl',
#     52: 'banana',
#     53: 'apple',
#     54: 'sandwich',
#     55: 'orange',
#     56: 'broccoli',
#     57: 'carrot',
#     58: 'hot dog',
#     59: 'pizza',
#     60: 'donut',
#     61: 'cake',
#     62: 'chair',
#     63: 'couch',
#     64: 'potted plant',
#     65: 'bed',
#     67: 'dining table',
#     70: 'toilet',
#     72: 'tv',
#     73: 'laptop',
#     74: 'mouse',
#     75: 'remote',
#     76: 'keyboard',
#     77: 'cell phone',
#     78: 'microwave',
#     79: 'oven',
#     80: 'toaster',
#     81: 'sink',
#     82: 'refrigerator',
#     84: 'book',
#     85: 'clock',
#     86: 'vase',
#     87: 'scissors',
#     88: 'teddy bear',
#     89: 'hair drier',
#     90: 'toothbrush'
# }
# ILSVRC_category_id = ['n02691156',
#                       'n02419796',
#                       'n02131653',
#                       'n02834778',
#                       'n01503061',
#                       'n02924116',
#                       'n02958343',
#                       'n02402425',
#                       'n02084071',
#                       'n02121808',
#                       'n02503517',
#                       'n02118333',
#                       'n02510455',
#                       'n02342885',
#                       'n02374451',
#                       'n02129165',
#                       'n01674464',
#                       'n02484322',
#                       'n03790512',
#                       'n02324045',
#                       'n02509815',
#                       'n02411705',
#                       'n01726692',
#                       'n02355227',
#                       'n02129604',
#                       'n04468005',
#                       'n01662784',
#                       'n04530566',
#                       'n02062744',
#                       'n02391049']
#
# ILSVRC_category = [
#     'airplane',
#     'antelope',
#     'bear',
#     'bicycle',
#     'bird',
#     'bus',
#     'car',
#     'cattle',
#     'dog',
#     'domestic_cat',
#     'elephant',
#     'fox',
#     'giant_panda',
#     'hamster',
#     'horse',
#     'lion',
#     'lizard',
#     'monkey',
#     'motorcycle',
#     'rabbit',
#     'red_panda',
#     'sheep',
#     'snake',
#     'squirrel',
#     'tiger',
#     'train',
#     'turtle',
#     'watercraft',
#     'whale',
#     'zebra']
ILSVRC_TO_COCO = {
    'n02374451': 19,
    'n02411705': 20,
    'n04468005': 7,
    'n02391049': 24,
    'n02131653': 23,
    'n02084071': 18,
    'n03790512': 4,
    'n02924116': 6,
    'n02958343': 3,
    'n02834778': 2,
    'n02503517': 22,
    'n02691156': 5,
    'n01503061': 16
}
ILSVRC_COCO_INTERSET = ['airplane',
                        'bear',
                        'bicycle',
                        'bird',
                        'bus',
                        'car',
                        'dog',
                        'elephant',
                        'horse',
                        'motorcycle',
                        'sheep',
                        'train',
                        'zebra']
# def map_ILSVRC_to_coco():
#     ILSVRC_to_coco_dict={}
#     ILSVRC_subset_based_on_coco=[]
#     coco_name_to_id_dict={v:k for k,v in coco_category_map.items()}
#     for id, name in zip(ILSVRC_category_id,ILSVRC_category):
#         if name in coco_name_to_id_dict:
#             ILSVRC_to_coco_dict[id]=coco_name_to_id_dict[name]
#             ILSVRC_subset_based_on_coco.append(name)
#     print(ILSVRC_to_coco_dict)
#     print(ILSVRC_subset_based_on_coco)
#
#
#
# if __name__=='__main__':
#     map_ILSVRC_to_coco()
