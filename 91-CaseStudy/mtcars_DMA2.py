#MT Cars Part2
#-----------------------------
#%
#Part -2 :
# use original mtcars : Groupby cyl and display rows 1 to 2
by_cyl =  mtcars.groupby('cyl')

#mean mpg
by_cyl['mpg'].mean()
slice(by_cyl, 1:3)


#group by gear and display top 2 (hghest) bottom 2 (lowest) by mpg
mtcars %>% arrange(gear, mpg) %>% select(gear, mpg, everything())
mtcars %>% group_by(gear) %>% top_n(n = 2, wt = mpg) %>% arrange(gear, mpg)
mtcars %>% group_by(gear) %>% top_n(n = -2, wt = mpg) %>% arrange(gear, mpg)

#Display selected Columns
#select vs, mpg and wt
mtcars %>% dplyr::select(vs, mpg, wt)
#select only those columns which contain 'vs'
select(mtcars, contains ='vs')

#Groupby summaries
#calculate mean mpg and max wt, grouped by am
mtcars %>% group_by(am) %>% summarise(mean(mpg), max(wt))
#mean displacement
summarise(mtcars, mean(disp))
#mean displacement grouped by cyl; create new names of summary columns
summarise(group_by(mtcars, cyl), mean(disp))
summarise(group_by(mtcars, cyl), m = mean(disp), sd = sd(disp))
#group by am and gear and find mean of all other columns
mtcars %>% group_by(am, gear) %>% summarise_all(mean)
#group by am and gear and find min and max of all other columns
mtcars %>% group_by(am, gear)%>% summarise_all(c("min", "max"))
#group by am and gear and find median of all other columns
mtcars %>% group_by(am, gear)%>% summarise_all(funs(med = median))
#calculate min and max of wt and gear
mtcars %>% select(wt, gear)%>% summarise_all(c("min", "max"))
#simple Summaries
#find mean of mpg and max of wt for all data
mtcars %>% summarise(mean(mpg), max(wt))
#find mean and median of all columns
mtcars %>% summarise_all(mean)
mtcars %>% summarise_all(funs(med = median))
#Find mean if columns are numeric; do it for mtcars and iris dataset
mtcars %>% summarise_if(is.numeric, mean, na.rm = TRUE)
iris %>% summarise_if(is.numeric, mean, na.rm = TRUE)
#find mean of mpg and wt, remove missing values if exists
mtcars %>% summarise_at(c("mpg", "wt"), mean, na.rm = TRUE)

#print all rows/ columns
#display all rows
tbl_df(mtcars) %>% print(n = Inf)
#display all columns
			tbl_df(mtcars) %>% print(width = Inf)
			tbl_df(mtcars) %>% as.data.frame(mtcars)
	#get sample rows
		#print random 20% of rows
			sample_frac(mtcars, 0.2, replace=F)
		#print random 5 rows
			sample_n(mtcars, 5, replace=F)
	#Other Queries
		#group by cyl, find average wt, average hp and arrange in decreasing order of avgerage mean, increasing order of average wt
			mtcars %>% group_by(cyl) %>% summarise(avgwt = mean(wt), meanhp = mean(hp)) %>% arrange( desc(meanhp), avgwt)
		#rows with last 2 mpg
			top_n(mtcars,-2, mpg)
		#find rank of each data in their respective columns
			mtcars %>% mutate_each( funs(min_rank))
		#shift one column right and left
			mtcars %>% lead()
			mtcars %>% lag()
		#bind rows/ columns
			bind_rows(mtcars, mtcars)
			bind_cols(mtcars,mtcars)
		# Selectt row in each group
			mtcars %>% group_by(cyl, am) %>% slice(1)
		#find how many cars with each gear type
			table(mtcars$gear)
		#create pivot table - giving count of cars - gear, cyl, am
			table(mtcars$gear, mtcars$cyl, mtcars$am)
			xtabs(~ gear + cyl + am, data=mtcars)
		#find correlation between mpg and wt
			cor(mtcars$mpg, mtcars$wt)
	#plots
		#create histogram of mpg
			hist(mtcars$mgp)
		#create boxplot of mpg wrt of gears
			boxplot(mpg ~ factor(gear), data=mtcars)
		#create barplot & pie using gear variable
			barplot(table(mtcars$gear))
			pie(table(mtcars$gear))
