CREATE TABLE `user` (
  `userid` int NOT NULL,
  `username` varchar(45) DEFAULT NULL,
  `groupid` int DEFAULT NULL,
  `groupname` varchar(45) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
)
CREATE TABLE `rights` (
  `rightsid` int NOT NULL,
  `rightsname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rightsid`)
)
CREATE TABLE `group` (
  `groupid` int NOT NULL,
  `groupname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`groupid`)
)
CREATE TABLE `group_rights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupid` varchar(45) DEFAULT NULL,
  `rightsid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
