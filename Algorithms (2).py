class Algorithms:
    def sortingAlgorithms(self , array,attribute ):
        return None


class BubbleSort(Algorithms):
    def sortingAlgorithms(self , array,attribute ):
        for i in range(1,len(array)):
            for k in range(len(array)-i):
                if(getattr(array[k],attribute)>getattr(array[k+1],attribute)):
                    key=array[k+1]
                    array[k+1]=array[k]
                    array[k]=key
        return array


class SelectionSort(Algorithms):
    def sortingAlgorithms(self , array,attribute ):
        for i in range(len(array)-1):
            for j in range(i,len(array)):
                if(getattr(array[j],attribute)<getattr(array[i],attribute)):
                    key=array[j]
                    array[j]=array[i]
                    array[i]=key
        return array

        

class InsertionSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):
        for i in range(1,len(array)):
            key=array[i]
            j=i-1
            while j>=0 and getattr(key,attribute)<getattr(array[j],attribute):
                array[j+1]=array[j]
                j-=1
            array[j+1]=key
        return array
        
class MergeSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):
        def Merge(start,m,end,array):
            n1=m-start+1
            n2=end-m
            l=[None]*(n1)
            r=[None]*(n2)
            for i in range(0,n1):
                l[i]=array[start+i]
            for i in range(0,n2):
                r[i]=array[m+1+i]
            i=0
            j=0
            k=start
            while i<n1 and j<n2:
                if(getattr(l[i],attribute)>getattr(r[j],attribute)):
                    array[k]=r[j]
                    j+=1
                    k+=1
                else:
                    array[k]=l[i]
                    i+=1
                    k+=1
            while i<n1:
                array[k]=l[i]
                i+=1
                k+=1
            while j<n2:
                array[k]=r[j]
                j+=1
                k+=1
        def MergeSort1(startInd,endInd,array):
            if(startInd<endInd):
                m=((endInd-1)+startInd)//2
                MergeSort1(startInd, m, array)
                MergeSort1(m+1, endInd, array)
                Merge(startInd,m,endInd,array)
            return array
        return MergeSort1(0,len(array)-1,array)

class CountingSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):
        if(attribute == "founded" or attribute == "world_rank" or attribute == "country_rank" ):
            
            large=array[0]
            b=[0]*len(array)
            for i in range(0,len(array)):
                if(getattr(large,attribute)<getattr(array[i],attribute)):
                    large=array[i]
            c=[0]*(getattr(large,attribute)+1)
            for i in range(0,len(array)):
                rn=getattr(array[i],attribute)
                c[rn]+=1
            for i in range(1,len(c)):
                c[i]+=c[i-1]
            for i in range(len(array)-1,-1,-1):
                b[c[getattr(array[i],attribute)]-1]=array[i]
                c[getattr(array[i],attribute)]=c[getattr(array[i],attribute)]-1
            return(b)
        
        else:
            
            
            b=[0]*len(array)
            c=[0]*27
            for i in range(len(array)):
                tempString = getattr(array[i],attribute)
                tempString = tempString.lower()
                #print(ord(tempString[0]) - 97)
                if(ord(tempString[0]) - 97>25 or ord(tempString[0]) - 97<0):
                    c[26]+=1
                else:
                    c[ord(tempString[0]) - 97]+=1
            
            for i in range(1,len(c)):
                c[i]+=c[i-1]
            
            #print(c)
            dec=len(array)
            for i in range(len(array)-1,-1,-1):
                temp=getattr(array[i],attribute)
                temp=temp.lower()
                count=(ord(temp[0])-97)
                if(count<=25 and count>=0 ):
                    b[c[count]-1]=array[i]
                    c[count]-=1
                else:
                    b[dec-1]=array[i]
                    c[26]-=1
                    dec-=1
                    
            return(b)

    
    
class RadixSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):

        def CountingSort(array,k,large):
            b=[0]*len(array)
            c=[0]*(getattr(large,attribute)+1)
            for i in range(0,len(array)):
                rn=getattr(array[i],attribute)
                c[(rn//k)%10]+=1
            for i in range(1,len(c)):
                c[i]+=c[i-1]
            for i in range(len(array)-1,-1,-1):
               b[c[((getattr(array[i],attribute)//k)%10)]-1]=array[i]
               c[(getattr(array[i],attribute)//k)%10]=c[(getattr(array[i],attribute)//k)%10]-1
            return(b)
        temp=1
        large=array[0]
        for i in range(0,len(array)):
            if(getattr(large,attribute)<int(getattr(array[i],attribute))):
                large=array[i]
        for i in range(0,len(str(getattr(large,attribute)))):
            array=CountingSort(array,temp,large)
            temp*=10
        return array

class BucketSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):
        import math
        def Scale(array):
            small=getattr(array[0],attribute)
            for i in range(0,len(array)):
                if(getattr(array[i],attribute)<small):
                    small=getattr(array[i],attribute)
            for i in range(0,len(array)):
                temp=getattr(array[i],attribute)+abs(small)
                setattr(array[i],attribute,temp)
            return array,small
        def ReScale(array,number):
            for i in range(0,len(array)):
                temp=getattr(array[i],attribute)-number
                setattr(array[i],attribute,temp)
            return array
        def InsertionSort(a):
            for i in range(1,len(a)):
                key=a[i]
                j=i-1
                while j>=0 and getattr(key,attribute)<getattr(a[j],attribute):
                    a[j+1]=a[j]
                    j-=1
                a[j+1]=key

        def findLarge(array):
            large=getattr(array[0],attribute)
            for i in range(0,len(array)):
                if(getattr(array[i],attribute)>large):
                    large=getattr(array[i],attribute)
            return large
        def BucketSort(array):
            array,small=Scale(array)
            n=len(array)
            bucketArray=[]
            for i in range(0,len(array)):
                bucketArray.append([])
            maxDigitLen=len(str(findLarge(array)))
            diviser=1
            for i in range(0,maxDigitLen):
                diviser*=10
            for i in range(0,len(array)):
                temp=getattr(array[i],attribute)/diviser
                setattr(array[i],attribute,temp)
            #print(array)
            for i in range(0,len(array)):
                bucketArray[math.floor(getattr(array[i],attribute)*len(array))].append(array[i])
            for i in bucketArray:
                InsertionSort(i)
            array=[]
            for i in bucketArray:
                array+=i
            for i in range(0,len(array)):
                temp=int(getattr(array[i],attribute)*diviser)
                setattr(array[i],attribute,temp) 
            return ReScale(array, small)
        return BucketSort(array)
    
class CombSort(Algorithms):
    def sortingAlgorithms(self,array,attribute):
        starter=int(len(array)-1)
        i=0
        j=int(starter)
        while starter>=1:
            if(getattr(array[i],attribute)>getattr(array[j],attribute)):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
            if(j==len(array)-1):
                starter=int(starter//1.3)
                j=starter
                i=0
            else:    
                i+=1
                j+=1
        return array

class FlashSort(Algorithms):
    def sortingAlgorithms(self,array,attribute):
        
        for i in range(len(array)):
            small = array[i]
            temp_index = i
            for j in range(i,len(array)):
                if(getattr(small,attribute) > getattr(array[j],attribute)):
                    #print(small)
                    
                    small = array[j]
                    temp_index = j
            temp = array[i]
            #print(temp_index)
            array[i] = small
            array[temp_index] = temp
        return array

class QuickSort(Algorithms):
    def sortingAlgorithms(self, array,attribute):
        def quickSort(array,low,high):
            if(low<high):
                p=partition(array,low,high)
                quickSort(array,low,p-1)
                quickSort(array,p+1,high)
            return array

        def partition(array,low,high):
            pivot=array[high]
            i=(low-1)
            for j in range(low,high):
                if(getattr(array[j],attribute)<getattr(pivot,attribute)):
                    i+=1
                    temp=array[i]
                    array[i]=array[j]
                    array[j]=temp


            temp=array[i+1]
            array[i+1]=array[high]
            array[high]=temp
            return(i+1)

        return quickSort(array,0,len(array)-1)
    


        
        
class ShellSort(Algorithms):
    def sortingAlgorithms(self , array ,attribute):
        gap=len(array)//2
        while gap>=1:
                for j in range(gap,len(array)):
                    temp=array[j]
                    i=j
                    while (i>=gap and getattr(array[i-gap],attribute)>getattr(temp,attribute)):
                        array[i]=array[i-gap]
                        i=i-gap
                    array[i]=temp
                gap=gap//2
        return array
        