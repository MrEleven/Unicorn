alter table `comment` add column `reply` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '回复评论的ID';
alter table `comment` add column `reply_user` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '被回复的用户Id';

CREATE TABLE `message` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `marker_id` bigint(20) unsigned NOT NULL COMMENT '帖子id',
  `comment_id` bigint(20) unsigned NOT NULL COMMENT '评论id',
  `receiver_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '接收者用户id',
  `create_time` datetime NOT NULL DEFAULT '2014-03-13 00:00:00' COMMENT '创建时间',
  `message_type` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `message` (`receiver_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;