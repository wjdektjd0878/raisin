CREATE TABLE `tb_user` (
  `user_id` int(10) unsigned NOT NULL AUTO_INCREMENT, 
  `user_google_id` varchar(50) NOT NULL COMMENT '유저 아이디',
  `nickname` varchar(50) NOT NULL COMMENT '게임 중 사용될 이름',
  `point` int(10) unsigned NOT NULL COMMENT '게임 중 얻은 포인트',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_chapter` (
  `chapter_id` int(10) unsigned NOT NULL AUTO_INCREMENT, 
  `chapter_category` varchar(50) NOT NULL COMMENT '챕터 유형',
  `chapter_detail` varchar(255) NOT NULL COMMENT '챕터 설명',
  PRIMARY KEY (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_game_session` (
  `user_id` int(10) unsigned NOT NULL COMMENT '유저 아이디',
  `session_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `start_time` datetime(6) NOT NULL COMMENT '세션 시작 타임',
  `end_time` datetime(6) NOT NULL COMMENT '세션 종료 타임',
  `session_end` varchar(1) NOT NULL COMMENT '세션 종료 여부 Y/N',
  PRIMARY KEY (`session_id`),
  FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_chapter_progress` (
  `progress_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `chapter_id` int(10) unsigned NOT NULL COMMENT '챕터 아이디',
  `user_id` int(10) unsigned NOT NULL COMMENT '유저 아이디',
  `success_whether` varchar(1) NOT NULL COMMENT '챕터 종료 여부 Y/N',
  PRIMARY KEY (`progress_id`),
  FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`user_id`),
  FOREIGN KEY (`chapter_id`) REFERENCES `tb_chapter` (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_story` (
  `story_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `chapter_id` int(10) unsigned NOT NULL COMMENT '챕터 아이디',
  `success_point` int(10) unsigned NOT NULL COMMENT '스토리 성공시 포인트 아이디',
  `story_detail` varchar(255) NOT NULL COMMENT '스토리 디테일',
  `story_type` varchar(5) NOT NULL COMMENT '메인/서브 스토리 구분',
  PRIMARY KEY (`story_id`),
  FOREIGN KEY (`chapter_id`) REFERENCES `tb_chapter` (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_ending` (
  `ending_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `chapter_id` int(10) unsigned NOT NULL COMMENT '챕터 아이디',
  `ending_detail` varchar(255) NOT NULL COMMENT '엔딩 디테일',
  PRIMARY KEY (`ending_id`),
  FOREIGN KEY (`chapter_id`) REFERENCES `tb_chapter` (`chapter_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_choice` (
  `choice_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `story_id` int(10) unsigned NOT NULL COMMENT '스토리 아이디',
  `choice_detail` varchar(255) NOT NULL COMMENT '선택 디테일',
  `success_point_standard` varchar(10) NOT NULL COMMENT '선택지 성공 가능 포인트',
  PRIMARY KEY (`choice_id`),
  FOREIGN KEY (`story_id`) REFERENCES `tb_story` (`story_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_game_progress` (
  `game_progress_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `story_id` int(10) unsigned NOT NULL COMMENT '스토리 아이디',
  `choice_id` int(10) unsigned NOT NULL COMMENT '선택지 아이디',
  `user_id` int(10) unsigned NOT NULL COMMENT '유저 아이디',
  `game_progress_success` varchar(10) NOT NULL COMMENT '진행 성공 여부 Y/N',
  PRIMARY KEY (`game_progress_id`),
  FOREIGN KEY (`story_id`) REFERENCES `tb_story` (`story_id`),
  FOREIGN KEY (`user_id`) REFERENCES `tb_user` (`user_id`),
  FOREIGN KEY (`choice_id`) REFERENCES `tb_choice` (`choice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tb_success_probability` (
  `success_percent` int(10) unsigned NOT NULL COMMENT '성공 확률',
  `choice_id` int(10) unsigned NOT NULL COMMENT '선택지 아이디',
  PRIMARY KEY (`success_percent`),
  FOREIGN KEY (`choice_id`) REFERENCES `tb_choice` (`choice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
