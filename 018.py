def FindTwoSum(nums,target):
    nums_dict={num:i for i,num in enumerate(nums)}
    answers=[]
    also_exsit=[]
    for i in range(len(nums)):
        t=nums_dict.get(target-nums[i])
        if t is not None and t!=i and t not in also_exsit: #存在并且不是原数，而且不能重复
            answers.append([nums[t],nums[i]])
            also_exsit.append(i)
            also_exsit.append(t)
    return answers

def FindFourSum(nums,target):
    answers = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                b=[]
                b[:]=nums[:]
                b.remove(nums[i])
                b.remove(nums[j])
                a=FindTwoSum(b,target-nums[i]-nums[j])
                if a is not None:
                    for zuhe in a:
                        zuhe.append(nums[i])
                        zuhe.append(nums[j])
                        answers.append(zuhe)
    answers_set=[]
    answers_over=[]
    for i in answers:
        if set(i) not in answers_set:
            answers_set.append(set(i))
            answers_over.append(i)

    return answers_over
a=FindTwoSum([1,2,3,4,-1,5,6,7],4)

b=FindFourSum([1, 0, -1, 0, -2, 2],0)