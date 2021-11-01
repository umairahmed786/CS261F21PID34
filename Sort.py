
      
def SortData(attribute,algorithm,order):
    from numpy import array

    import Algorithms
    import pandas as pd
    df = pd.read_csv('University2.csv')
    name=df.Name.values.tolist()
    acronym=df.Acronym.values.tolist()
    address=df.Address.values.tolist()
    founded=df.Founded.values.tolist()
    motto=df.Motto.values.tolist()
    worldRank=df.WorldRank.values.tolist()
    countryRank=df.CountryRank.values.tolist()
    phone=df.Phone.values.tolist()
    fax=df.Fax.values.tolist()



    class University():
        Name=""
        Acronym=""
        Address=""
        Founded=0
        Motto=""
        WorldRank=0
        CountryRank=0
        Phone=""
        Fax=""
        def __init__(self,name,acronym,address,founded,motto,worldRank,countryRank,phone,fax):
            self.Name=name
            self.Acronym=acronym
            self.Address=address
            self.Founded=founded
            self.Motto=motto
            self.WorldRank=worldRank
            self.CountryRank=countryRank
            self.Phone=phone
            self.Fax=fax
    totalUniversities=[]
    for i in range(0,len(name)):
        ob=University(name[i],acronym[i],address[i],founded[i],motto[i],worldRank[i],countryRank[i],phone[i],fax[i])
        totalUniversities.append(ob)




    obj=Algorithms.Algorithms()
    
    if(algorithm == "MergeSort"):
        obj=Algorithms.MergeSort()
    elif(algorithm=="InsertionSort"):
        obj=Algorithms.InsertionSort()
    elif(algorithm=="SelectionSort"):
        obj=Algorithms.SelectionSort()
    elif(algorithm=="BubbleSort"):
        obj=Algorithms.BubbleSort()
    elif(algorithm=="QuickSort"):
        obj=Algorithms.QuickSort()
    elif(algorithm=="CountingSort"):
        obj=Algorithms.CountingSort()
    elif(algorithm=="RadixSort"):
        obj=Algorithms.RadixSort()
    elif(algorithm=="BucketSort"):
        obj=Algorithms.BucketSort()
    elif(algorithm=="ShellSort"):
        obj=Algorithms.ShellSort()
    elif(algorithm=="CombSort"):
        obj=Algorithms.CombSort()
    elif(algorithm=="FlashSort"):
        obj=Algorithms.FlashSort()

    array=obj.sortingAlgorithms(totalUniversities,attribute)
    if(order=="Descending"):
        array=array[::-1]
    name=[]
    acronym=[]
    address=[]
    founded=[]
    motto=[]
    worldRank=[]
    countryRank=[]
    phone=[]
    fax=[]
    for i in array:
        name.append(i.Name)
        acronym.append(i.Acronym)
        address.append(i.Address)
        founded.append(i.Founded)
        motto.append(i.Motto)
        worldRank.append(i.WorldRank)
        countryRank.append(i.CountryRank)
        phone.append(i.Phone)
        fax.append(i.Fax)

    df = pd.DataFrame({'Name':name, 'Acronym':acronym, 'Address':address,'Founded':founded,'Motto':motto,'WorldRank':worldRank,'CountryRank':countryRank,'Phone':phone,'Fax':fax})
    df.to_csv('University3.csv', index=False, encoding='utf-8')

    