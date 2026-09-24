import pandas as pd

s = pd.Series(["a", "b", "c", "d", "e"], index=[1, 2, 3, 4, 5])
print(s)
print("透過索引標籤存取單一元素",s[1])  
print("透過位置存取單一元素",s.iloc[0])    
print("透過索引標籤存取多個元素",s[[1, 2, 3]])  
print("透過位置存取多個元素",s.iloc[[0, 1, 2]])     
print("透過索引標籤存取多個元素（使用 loc）",s.loc[[1, 2, 3]])