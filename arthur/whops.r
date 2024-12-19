library(ggplot2)


df.main <- read.csv(
    fileEncoding = 'latin1',
    na.strings = c('NA', ''),
    file = './arthur/base_2.csv',
    sep = ';',
    dec = ','
)

print(colnames(df.main))