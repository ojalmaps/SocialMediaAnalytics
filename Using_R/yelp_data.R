library(ggplot2)
business_data = read.csv(file ="C:/College/Summer 2021/webscraping/Resources/business_csv_data.csv")
head(business_data)

ggplot(business_data) + geom_bar(aes(x=state), fill ="red")
ggplot(business_data) + geom_bar(aes(x=stars), fill ="blue")

ggplot(data = business_data, aes(x = factor(1), fill = factor(stars)))+ geom_bar(width=1)+ coord_polar(theta = "y")

user_data = read.csv(file ="C:/College/Summer 2021/webscraping/Resources/yelp_user_data.csv")

user_votes = user_data[,c("cool_votes","funny_votes","useful_votes")]
cor(user_data$funny_votes, user_data$fans)

model.lm = lm(useful_vptes ~ review_count + fans, data=user_data)