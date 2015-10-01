CREATE TABLE `marker` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(48) NOT NULL DEFAULT '' COMMENT '主题',
  `marker` varchar(1024) NOT NULL DEFAULT '' COMMENT '签到内容',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='签到'