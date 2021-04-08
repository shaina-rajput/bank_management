-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2020 at 01:06 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bankmanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `fristname` varchar(255) DEFAULT NULL,
  `middlename` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `accountno` varchar(255) DEFAULT NULL,
  `accountcreated` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phoneno` varchar(255) DEFAULT NULL,
  `aadharno` varchar(255) DEFAULT NULL,
  `closingbalance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`fristname`, `middlename`, `lastname`, `accountno`, `accountcreated`, `email`, `phoneno`, `aadharno`, `closingbalance`) VALUES
('shaina', '-', 'rajput', '11', '2020-07-01 23:04:22.148796', 'shainarajput3100@gmail.com', '9868444803', '457387', 12000),
('dinesh', 'prakash', 'verma', '12', '2020-07-03 11:01:34.168707', 'dineshprakashverma@gmail.com', '9540411094', '56575', 3531),
('shivansh', '-', 'rajput', '14', '2020-07-02 12:58:54.491908', 'gamingwithshivanshpro@gmail.com', '7011880134', '6576453', 40000),
('prachi', '-', 'rajput', '16', '2020-07-03 11:04:30.983821', 'prachirajput2611@gmail.com', '9416316082', '76583495', 599500),
('ritika', '-', 'rana', '17', '2020-07-03 16:31:44.284440', 'ritikarajput1405@gmail.com', '7037233375', '8456834', 50000),
('seema', '-', 'verma', '18', '2020-07-03 16:35:23.841998', 'shainarajput3100@gmail.com', '7011880134', '65787', 64837);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
