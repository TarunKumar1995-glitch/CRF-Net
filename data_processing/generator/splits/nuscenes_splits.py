"""
This scripts provides scenes for train, validation and test data on nuscenes data set.
They are randomly chosen in a way that the percentage of night and rain data is equal in every set.
"""
import random
import os
import sys
import argparse

# Allow relative imports when being executed as script.
if __name__ == "__main__" and not __package__:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..','..', '..', '..'))
    import crfnet  # noqa: F401
    __package__ = "crfnet"

from crfnet.utils.config import get_config

class Scenes:
    def __init__(self, train, val, test, test_rain, test_night):
        self.train   = train
        self.val = val
        self.test  = test
        self.test_rain  = test_rain
        self.test_night = test_night
    

FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) 

# Parse arguments
FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) 

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default=os.path.join(FILE_DIRECTORY,"configs/nuscenes_sample.cfg"))
parser.add_argument('--model', type=str, default="./saved_models/nuscenes_sample.h5")
parser.add_argument('--st', type=float, default=None)
parser.add_argument('--render', default=False, action='store_true')
parser.add_argument('--eval_from_detection_pickle', default=False, action='store_true')
args = parser.parse_args()

if not os.path.exists(args.config):
    raise FileNotFoundError("ERROR: Config file \"%s\" not found"%(args.config))
else:
    cfg = get_config(args.config)

random.seed(42)
# no_scenes=85*cfg.no_data_sets
no_scenes=85
complete_data=random.sample(range(0,no_scenes),no_scenes)
train=complete_data[0:int(0.6*no_scenes)]
train=sorted(train)
val=complete_data[int(0.6*no_scenes):int(0.8*no_scenes)]
val=sorted(val)
test=complete_data[int(0.8*no_scenes):]
test=sorted(test)
print("train data set", train)
print("test data set", test)
print("validation data set", val)

Scenes.default = Scenes(
    # train = [0,2,3,4,5,7,9,10,12,15,16,17,19,21,22,24,25,26,27,28,30,32,34,38,42,43,44,45,47,48,49,50,52,53,54,55,56,57,58,62,65,66,68,71,72,73,76,77,79,80,83,85,88,90,98,100,105,106,108,109,110,114,115,116,117,118,119,120,121,123,125,126,129,130,131,132,134,135,136,137,139,140,141,144,146,148,149,151,152,155,156,157,160,161,162,163,164,165,167,168,169,172,173,174,176,177,178,181,184,185,186,187,192,194,196,197,199,201,202,203,204,205,206,207,210,211,212,213,214,215,216,219,221,222,224,225,228,229,230,231,232,233,235,236,237,238,242,243,248,250,251,252,253,254,255,258,259,261,262,263,264,267,268,269,270,272,274,275,276,277,279,280,283,284,285,286,289,290,292,295,296,299,301,303,304,306,307,309,311,314,315,316,318,319,320,321,326,328,329,330,334,335,337,339,342,343,345,349,350,351,352,356,358,359,361,367,368,370,371,374,378,379,381,382,384,385,387,388,389,390,391,392,393,396,397,400,401,405,406,407,408,410,412,413,414,417,418,419,420,421,422,423,424,425,426,428,430,432,433,434,435,438,439,441,444,447,448,449,451,452,453,455,456,460,461,462,463,464,465,467,469,472,473,474,475,477,479,480,481,482,483,484,485,486,487,488,490,492,493,494,495,496,497,498,499,500,503,504,509,512,513,515,516,517,521,524,526,527,528,529,531,532,539,540,542,543,544,545,547,549,552,553,555,556,559,560,562,563,565,566,568,569,570,572,575,577,578,579,582,583,584,585,586,587,589,591,593,595,596,599,600,602,603,604,605,607,608,610,612,615,618,619,621,622,624,625,626,627,628,629,630,631,636,637,638,640,641,642,644,646,647,650,652,655,656,657,664,665,667,668,669,670,671,673,674,675,678,683,684,688,689,690,691,692,694,695,696,697,699,702,703,704,705,706,708,709,711,712,713,717,718,720,723,724,725,726,728,729,730,732,733,734,737,738,739,741,744,746,747,748,749,752,753,754,755,756,757,758,759,760,761,763,764,766,767,768,771,772,775,776,779,780,781,783,784,786,787,790,791,792,793,795,797,798,800,801,803,807,813,815,816,818,819,823,824,825,827,833,834,835,836,837,838,841,842,843,845,847,848,849],
    # val= [1,8,14,31,33,39,41,51,59,63,64,70,74,75,82,84,87,91,93,95,97,101,103,111,112,124,127,133,138,142,143,145,150,153,166,170,171,188,190,191,193,195,208,209,218,220,223,227,241,244,247,249,256,265,266,281,282,288,294,297,298,300,308,310,313,317,322,323,324,327,333,338,340,341,357,360,362,364,365,366,373,375,377,380,383,394,398,399,402,403,411,431,437,443,445,450,466,468,471,478,491,505,507,510,522,523,525,530,537,546,548,551,554,576,580,581,588,590,594,597,598,601,609,613,616,623,632,634,649,651,653,654,660,661,662,677,679,681,682,686,687,700,707,710,714,716,722,735,742,750,762,769,770,773,774,782,794,796,802,804,806,808,809,810,817,822,828,831,839,840],
    # test= [6,11,13,18,20,23,29,35,36,37,40,46,60,61,67,69,78,81,86,89,92,94,96,99,102,104,107,113,122,128,147,154,158,159,175,179,180,182,183,189,198,200,217,226,234,239,240,245,246,257,260,271,273,278,287,291,293,302,305,312,325,331,332,336,344,346,347,348,353,354,355,363,369,372,376,386,395,404,409,415,416,427,429,436,440,442,446,454,457,458,459,470,476,489,501,502,506,508,511,514,518,519,520,533,534,535,536,538,541,550,557,558,561,564,567,571,573,574,592,606,611,614,617,620,633,635,639,643,645,648,658,659,663,666,672,676,680,685,693,698,701,715,719,721,727,731,736,740,743,745,751,765,777,778,785,788,789,799,805,811,812,814,820,821,826,829,830,832,844,846],
    # test_rain= [354,355,363,369,372,376,386,454,457,458,459,470,476,489,501,502,506,633,635,658,659,663,666,672,676,680,685,693,698,701],
    # test_night= [751,765,777,778,785,788,789,799,805,811,812,814,820,821,826,829,830,832,844,846]
    
    # train = [0,2,3,4,5,7,9,10,12,15,16,17,19,21,22,24,25,26,27,28,30,32,34,38,42,43,44,45,47,48,49,50,52,53,54,55,56,57,58,62,65,66,68,71,72,73,76,77,79,80,83],
    # val= [1,8,14,31,33,39,41,51,59,63,64,70,74,75,82,84],
    # test= [6,11,13,18,20,23,29,35,36,37,40,46,60,61,67,69,78,81],
    train=complete_data[0:int(0.6*85)],
    val=complete_data[int(0.6*85):int(0.8*85)],
    test=complete_data[int(0.8*85):],
    test_rain= [0],
    test_night= [0]
)

### Debug scenes
Scenes.debug = Scenes(
    train= [0,2,3,5,7,9],
    val= [1,8],
    test= [4,6],
    test_rain= [0],
    test_night= [0]
)