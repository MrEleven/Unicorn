alter table `marker` add column `comment_count` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '评论数' after `marker`;

CREATE TABLE `comment` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'user_id',
  `marker_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '签到id',
  `content` varchar(1024) NOT NULL DEFAULT '' COMMENT '评论内容',
  `create_time` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='评论';