import random
random.seed(42)
complete_data=random.sample(range(0,85),85)
train=complete_data[0:int(0.6*85)]
train=sorted(train)
val=complete_data[int(0.6*85):int(0.8*85)]
val=sorted(val)
test=complete_data[int(0.8*85):]
test=sorted(test)
print("train data set", train)
print("test data set", test)
print("validation data set", val)