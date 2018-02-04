setwd("/home/abinash/Dropbox/peaky blenders/mutual funds files")
aditya<-read.csv("Uti.csv")
aditya_risk<-read.csv("uti_risk.csv")
aditya_risk<-aditya_risk[,-1]
aditya$P_n<-gsub(" ", "",aditya$Plan_name)
aditya_risk$Plan_name<-gsub(" ", "",aditya_risk$Plan_name)
aditya<-merge(aditya, aditya_risk, by.x ="P_n", by.y = "Plan_name", all.x = TRUE)

aditya<-aditya[,c(-1,-2)]
write.csv(aditya, "Uti.csv", row.names = FALSE)