library(ggplot2)

#df = read.table(file.choose(), header = TRUE, sep =",") # allows us to choose file 
#View(df)
#brain_data = df["Brain"]
#print(summary(brain_data))

# Loads data into data frame 
cust_data = read.table(file.choose(), header = TRUE, sep ="\t") # allows us to choose file 
View(cust_data) 

# Displaying some basic graphs
ggplot(cust_data)+ geom_histogram(aes(x = age), binwidth =  5)
ggplot(cust_data) + geom_bar(aes(x = sex))

# Display categories for the given x value 
ggplot(cust_data) + geom_bar(aes(x = marital.stat)) # graphs all the difference martial status
ggplot(cust_data) + geom_bar(aes(x = state.of.res))

# Displays the correlation between 2 columns 
cor(cust_data$age, cust_data$income)

# We can use the subset command to filter through and find relevant information 
# Here we want to load when income is positive
# This is a new data frame with relevant data 
data2 = subset(cust_data, (cust_data$age>15 & cust_data$income > 100 ))

cor(data2$age, data2$income)