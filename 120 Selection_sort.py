def selectionSort(List):
    for i in range(len(List)-1):
        minimum=i
        for j in range(i+1,len(List)):
            if (List[j]<List[minimum]):
                minimum=j
        if(minimum!=i):
            List[i],List[minimum]=List[minimum],List[i]
    return List

if __name__=='__main__':
    List=[2,56,90,87,65,45,33,78]
    print("sorted list:",selectionSort(List))