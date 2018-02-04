setwd("/home/abinash/Dropbox/peaky blenders/mutual funds files")

library(zoo)
library(ggplot2)
library(plyr)
library(dplyr)

aditya1<-read.csv("Aditya.csv")
aditya1<-aditya1[,129:168]
for(i in 0:19){
  aditya1[,2*i+1]=as.Date(as.yearmon(aditya1[,2*i+1], "%b-%y"))
}
aditya_date<-as.list(c())
aditya_value<-as.list(c())
for(i in 1:20) {
  aditya_date<-c(aditya_date, as.list(aditya1[,2*i-1]))
  aditya_value<-c(aditya_value, as.list(aditya1[,2*i]))
}
aditya_date<-as.Date(unlist(aditya_date))
aditya_value<-as.numeric(gsub(",", "", as.character(unlist(aditya_value))))
dp_aditya<-data.frame(aditya_date, aditya_value)
dp<-dp[!is.na(dp$aditya_date),]
date_mean_aditya<-ddply(dp,~aditya_date,summarise,Mean_Asset=mean(aditya_value))

hdfc1<-read.csv("HDFC.csv")
hdfc1<-hdfc1[,129:168]
for(i in 0:19){
  hdfc1[,2*i+1]=as.Date(as.yearmon(hdfc1[,2*i+1], "%b-%y"))
}
hdfc_date<-as.list(c())
hdfc_value<-as.list(c())
for(i in 1:20) {
  hdfc_date<-c(hdfc_date, as.list(hdfc1[,2*i-1]))
  hdfc_value<-c(hdfc_value, as.list(hdfc1[,2*i]))
}
hdfc_date<-as.Date(unlist(hdfc_date))
hdfc_value<-as.numeric(gsub(",", "", as.character(unlist(hdfc_value))))
dp<-data.frame(hdfc_date, hdfc_value)
dp<-dp[!is.na(dp$hdfc_date),]
date_mean_hdfc<-ddply(dp,~hdfc_date,summarise,Mean_Asset=mean(hdfc_value))


icici1<-read.csv("ICICI.csv")
icici1<-icici1[,130:169]
for(i in 0:19){
  icici1[,2*i+1]=as.Date(as.yearmon(icici1[,2*i+1], "%b-%y"))
}
icici_date<-as.list(c())
icici_value<-as.list(c())
for(i in 1:20) {
  icici_date<-c(icici_date, as.list(icici1[,2*i-1]))
  icici_value<-c(icici_value, as.list(icici1[,2*i]))
}
icici_date<-as.Date(unlist(icici_date))
icici_value<-as.numeric(gsub(",", "", as.character(unlist(icici_value))))
dp<-data.frame(icici_date, icici_value)
dp<-dp[!is.na(dp$icici_date),]
date_mean_icici<-ddply(dp,~icici_date,summarise,Mean_Asset=mean(icici_value))


reliance1<-read.csv("Reliance.csv")
reliance1<-reliance1[,130:169]
for(i in 0:19){
  reliance1[,2*i+1]=as.Date(as.yearmon(reliance1[,2*i+1], "%b-%y"))
}
reliance_date<-as.list(c())
reliance_value<-as.list(c())
for(i in 1:20) {
  reliance_date<-c(reliance_date, as.list(reliance1[,2*i-1]))
  reliance_value<-c(reliance_value, as.list(reliance1[,2*i]))
}
reliance_date<-as.Date(unlist(reliance_date))
reliance_value<-as.numeric(gsub(",", "", as.character(unlist(reliance_value))))
dp<-data.frame(reliance_date, reliance_value)
dp<-dp[!is.na(dp$reliance_date),]
date_mean_reliance<-ddply(dp,~reliance_date,summarise,Mean_Asset=mean(reliance_value))


sbi1<-read.csv("SBI.csv")
sbi1<-sbi1[,130:169]
for(i in 0:19){
  sbi1[,2*i+1]=as.Date(as.yearmon(sbi1[,2*i+1], "%b-%y"))
}
sbi_date<-as.list(c())
sbi_value<-as.list(c())
for(i in 1:20) {
  sbi_date<-c(sbi_date, as.list(sbi1[,2*i-1]))
  sbi_value<-c(sbi_value, as.list(sbi1[,2*i]))
}
sbi_date<-as.Date(unlist(sbi_date))
sbi_value<-as.numeric(gsub(",", "", as.character(unlist(sbi_value))))
dp<-data.frame(sbi_date, sbi_value)
dp<-dp[!is.na(dp$sbi_date),]
date_mean_sbi<-ddply(dp,~sbi_date,summarise,Mean_Asset=mean(sbi_value))


sundaram1<-read.csv("Sundaram.csv")
sundaram1<-sundaram1[,129:168]
for(i in 0:19){
  sundaram1[,2*i+1]=as.Date(as.yearmon(sundaram1[,2*i+1], "%b-%y"))
}
sundaram_date<-as.list(c())
sundaram_value<-as.list(c())
for(i in 1:20) {
  sundaram_date<-c(sundaram_date, as.list(sundaram1[,2*i-1]))
  sundaram_value<-c(sundaram_value, as.list(sundaram1[,2*i]))
}
sundaram_date<-as.Date(unlist(sundaram_date))
sundaram_value<-as.numeric(gsub(",", "", as.character(unlist(sundaram_value))))
dp<-data.frame(sundaram_date, sundaram_value)
dp<-dp[!is.na(dp$sundaram_date),]
date_mean_sundaram<-ddply(dp,~sundaram_date,summarise,Mean_Asset=mean(sundaram_value))


tata1<-read.csv("Tata.csv")
tata1<-tata1[,130:169]
for(i in 0:19){
  tata1[,2*i+1]=as.Date(as.yearmon(tata1[,2*i+1], "%b-%y"))
}
tata_date<-as.list(c())
tata_value<-as.list(c())
for(i in 1:20) {
  tata_date<-c(tata_date, as.list(tata1[,2*i-1]))
  tata_value<-c(tata_value, as.list(tata1[,2*i]))
}
tata_date<-as.Date(unlist(tata_date))
tata_value<-as.numeric(gsub(",", "", as.character(unlist(tata_value))))
dp<-data.frame(tata_date, tata_value)
dp<-dp[!is.na(dp$tata_date),]
date_mean_tata<-ddply(dp,~tata_date,summarise,Mean_Asset=mean(tata_value))


uti1<-read.csv("Uti.csv")
uti1<-uti1[,129:168]
for(i in 0:19){
  uti1[,2*i+1]=as.Date(as.yearmon(uti1[,2*i+1], "%b-%y"))
}
uti_date<-as.list(c())
uti_value<-as.list(c())
for(i in 1:20) {
  uti_date<-c(uti_date, as.list(uti1[,2*i-1]))
  uti_value<-c(uti_value, as.list(uti1[,2*i]))
}
uti_date<-as.Date(unlist(uti_date))
uti_value<-as.numeric(gsub(",", "", as.character(unlist(uti_value))))
dp<-data.frame(uti_date, uti_value)
dp<-dp[!is.na(dp$uti_date),]
date_mean_uti<-ddply(dp,~uti_date,summarise,Mean_Asset=mean(uti_value))

write.csv(date_mean_aditya, "Aditya_asset.csv", row.names = FALSE)
write.csv(date_mean_hdfc, "HDFC_asset.csv", row.names = FALSE)
write.csv(date_mean_icici, "ICICI_asset.csv", row.names = FALSE)
write.csv(date_mean_reliance, "Reliance_asset.csv", row.names = FALSE)
write.csv(date_mean_sbi, "SBI_asset.csv", row.names = FALSE)
write.csv(date_mean_sundaram, "Sundaram_asset.csv", row.names = FALSE)
write.csv(date_mean_tata, "TATA_asset.csv", row.names = FALSE)
write.csv(date_mean_uti, "UTI_asset.csv", row.names = FALSE)
