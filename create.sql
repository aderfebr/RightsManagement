CREATE TABLE `group` (
  `groupid` int NOT NULL,
  `groupname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`groupid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `group_rights` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupid` varchar(45) DEFAULT NULL,
  `rightsid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `menu` (
  `id` int NOT NULL,
  `label` varchar(45) DEFAULT NULL,
  `icon` varchar(45) DEFAULT NULL,
  `vis` varchar(45) DEFAULT NULL,
  `index` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `rights` (
  `rightsid` int NOT NULL,
  `rightsname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rightsid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `token` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(45) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `user` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `groupid` int DEFAULT NULL,
  `groupname` varchar(45) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `vis`, `index`) VALUES ('1', '主页', 'HomeFilled', 'True', '/home');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `vis`, `index`) VALUES ('2', '用户管理', 'UserFilled', 'True', '/user');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `vis`, `index`) VALUES ('3', '角色管理', 'MoreFilled', 'True', '/group');
INSERT INTO `rightsmanagement`.`menu` (`id`, `label`, `icon`, `vis`, `index`) VALUES ('4', '菜单管理', 'Operation', 'True', '/menu');
INSERT INTO `rightsmanagement`.`group` (`groupid`, `groupname`) VALUES ('1', 'student');
INSERT INTO `rightsmanagement`.`group` (`groupid`, `groupname`) VALUES ('2', 'teacher');
INSERT INTO `rightsmanagement`.`rights` (`rightsid`, `rightsname`) VALUES ('1', '查看用户');
INSERT INTO `rightsmanagement`.`group_rights` (`groupid`, `rightsid`) VALUES ('1', '1');