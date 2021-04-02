v1 <- 1:10
v2 <- 10:1
print(v1)
v2
v3 <- 100
v3
v1 <- c(4, 1, 8, 6, 10) # c()함수에는 아규먼트를 원하는 만큼 전달 가능 
v2 <- c(100, 200, TRUE, FALSE); print(v2)
v3 <- c("100", 200, T, F); print(v3)
v1[5]; v1[3]; v1[1]; v1[0]; v1[6]
length(v3)

rep(1, 100)
rep(1:3, 5)
rep(1:3, times=5) # 키워드 파라미터
rep(1:3, each=5)
?rep  #help()

LETTERS
letters
month.name
month.abb
pi

LETTERS;letters;month.name;month.abb;pi

LETTERS[1]; LETTERS[c(3,4,5)]
LETTERS[3:5]; LETTERS[5:3]
LETTERS[-1]; LETTERS[c(-2,-4)] # 음의값 인덱스: 해당 음의 값을 제외

length(LETTERS)
length(month.name)
length(pi)


x <- c(10,2,7,4,15)
x
print(x)
class(x)
rev(x) # 뒤에서 부터 출력 
range(x)
sort(x) # 정렬, 기본값은 오름차순
sort(x, decreasing = TRUE) # 내림차순
sort(x, decreasing = T)
#x <- sort(x)
order(x) # 정렬한 후 위치값(인덱스)을 반환, 기본값은 오름차순
order(x, decreasing = T) # 내림차순 정렬한 후 위치값 반환


x[3] <- 20
x
x + 1
x <- x + 1
max(x);min(x);mean(x);sum(x)
summary(x)

x[c(2,4)] # x[2], x[4]
x[c(F,T,F,T,F)] # x[c(T,F)] --> x[c(T,F,T,F,T)] 
x > 5
x[x > 5] 
x[x > 5 & x < 15] # x[x > 5 && x < 15]:&&는 하나의 값(첫째값)만 가지고 (비교)연산. 따라서 첫째값인 10이 TRUE이므로 모든 값 반환
#x[x > 5 | x < 15]

names(x)
names(x) <- LETTERS[1:5]
names(x) <- NULL
x[2];x["B"]; 


# &, &&
c(T, T, F, F) & c(T, F, T, F)
c(T, T, F, F) | c(T, F, T, F)
c(T, T, F, F) && c(T, F, T, F)
c(T, T, F, F) || c(T, F, T, F)


ls() # 객체 리스트 
rm(x) # 해당 객체 삭제 
x
class(x)

rainfall <- c(21.6, 23.6, 45.8, 77.0, 
              102.2, 133.3,327.9, 348.0, 
              137.6, 49.3, 53.0, 24.9)
rainfall > 100
rainfall[rainfall > 100]
which(rainfall > 100) #조건에 대해 TRUE에 해당하는 index를 출력
month.name[which(rainfall > 100)]
month.abb[which(rainfall > 100)]
month.korname <- c("1월","2월","3월",
                   "4월","5월","6월",
                   "7월","8월","9월",
                   "10월","11월","12월")
month.korname[which(rainfall > 100)]
which.max(rainfall) # max값 index
which.min(rainfall) # min값 index
month.korname[which.max(rainfall)]
month.korname[which.min(rainfall)]


sample(1:20, 3) 
sample(1:45, 6)
sample(1:10, 7)
sample(1:10, 7, replace=T) # replace=T는 중복허용 

paste("I'm","Duli","!!") # sep 기본값은 공백
paste("I'm","Duli","!!", sep="")
paste0("I'm","Duli","!!") # paste0는 공백 없음

fruit <- c("Apple", "Banana", "Strawberry")
food <- c("Pie","Juice", "Cake")
paste(fruit, food)

paste(fruit, food, sep="")
paste(fruit, food, sep=":::")
paste(fruit, food, sep="", collapse="-")
paste(fruit, food, sep="", collapse="")
paste(fruit, food, collapse=",")






