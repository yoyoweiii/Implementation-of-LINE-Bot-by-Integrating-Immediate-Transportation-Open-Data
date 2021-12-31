-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 產生時間： 2017 年 12 月 27 日 17:35
-- 伺服器版本: 5.7.18-0ubuntu0.16.04.1
-- PHP 版本： 7.0.18-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `1968`
--

-- --------------------------------------------------------

--
-- 資料表結構 `1968`
--

CREATE TABLE `1968` (
  `inc_type_name` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_name` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_time` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `incidentId` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `freewayId` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expresswayId` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `directionId` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_location` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `from_milepost` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `to_milepost` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interchange` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_blockage` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_severity` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_notify_time` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_notify_mode` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_end_time` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_stepNo` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `inc_step_time` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `notification`
--

CREATE TABLE `notification` (
  `user_id` text CHARACTER SET utf8 COLLATE utf8_bin,
  `begin` text CHARACTER SET utf8 COLLATE utf8_bin,
  `destination` text CHARACTER SET utf8 COLLATE utf8_bin,
  `occured_time` text CHARACTER SET utf8 COLLATE utf8_bin
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 資料表的匯出資料 `notification`
--

INSERT INTO `notification` (`user_id`, `begin`, `destination`, `occured_time`) VALUES
('Ua4ac720a3d0f48e77dda9d7c912cb5ad', '1&begin', '10&end', '12-17 19:48:00'),
('U0eff75124de2a8636262035ede5c5e4b', 'beginTaipei', NULL, '10-17 13:15:15'),
('Ub5357fe1a2c75eae8b3cb14d034b8d00', '3&begin', '10&end', '12-17 19:40:02');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
