library(ggplot2)

# Performing Analysis on the Yelp Business Data
business_data = read.csv(file ="C:/College/Summer 2021/webscraping/Resources/business_csv_data.csv")
head(business_data)

ggplot(business_data) + geom_bar(aes(x=state), fill ="red") # plot by each state
ggplot(business_data) + geom_bar(aes(x=stars), fill ="blue") # plot by average rating. 

ggplot(data = business_data, aes(x = factor(1), fill = factor(stars)))+ geom_bar(width=1)+ coord_polar(theta = "y")
# plotting a circular graph for the variable star. 


# Performing analysis on the Yelp User data. 
user_data = read.csv(file ="C:/College/Summer 2021/webscraping/Resources/yelp_user_data.csv")
user_votes = user_data[,c("cool_votes","funny_votes","useful_votes")]

cor(user_data$funny_votes, user_data$fans) # correlation between funny votes and fans. 

#lm - stands for linear model 
model.lm = lm(useful_votes ~ review_count + fans, data=user_data) # checking how useful votes is related to review count and fans. 
# In this scenario useful votes is the dependent variable and fans + review count are independent

coeffs = coefficients(model.lm) # extracting coefficient

ggplot(user_data) + geom_area()
#ggplot(business_data) + geom_bar(aes(x = review_count) + geom_plot()+ xlim(10, 2000)+ ylim(0,6000))

# Creating 3 clusters and plotting them 
userCluster = kmeans(user_data[1:1000,3:11],3) # from column 3 - 11 , excluding the names and id's 
ggplot(user_data,aes(review_count,fans, color =userCluster$cluster))+ geom_point()

