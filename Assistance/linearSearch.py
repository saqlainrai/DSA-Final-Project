import pandas as pd

def linearSearch(data, searchElement,index):
    '''
        data = 2d array
        searchElement = word or query being searched
        index = the index of column in which search is performed
    '''
    see=[]
    for i in range(0, len(data)):
        # -------we use .lower function that convert string into small caps by doing this 
        # -------we over come the  case sencetive 
        if searchElement.lower() in data[i][index].lower():
            see.append(data[i])

    #see = pd.DataFrame(see,columns=["Product Name","Price","Condition","Shipping Price","Shipping City","Seller name","Feedback","Rating"])
    return see


if __name__ == "__main__":
    data = pd.read_csv("medicineData.csv")
    data = data.values.tolist()
    found=linearSearch(data,"sleep",0)
    for row in found:
        print(row)
