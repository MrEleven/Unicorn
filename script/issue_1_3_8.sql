CREATE TABLE `bg` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(256) NOT NULL DEFAULT '' COMMENT '图片url',
  `type` int (3) unsigned NOT NULL DEFAULT '1' COMMENT '类型 1.pc 2.mobile',
  `status` int (3) unsigned NOT NULL DEFAULT '0' COMMENT '状态 1.有效 2.无效',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='背景';