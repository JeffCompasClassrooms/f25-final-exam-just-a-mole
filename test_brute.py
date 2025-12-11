import unittest
import pytest
import random
import time
from brute import Brute


class TestBruteOnce(unittest.TestCase):
    def test_init_not_string(self):
        with self.assertRaises(TypeError):
            brute = Brute(123)

    def test_hash_normal(self):
        brute = Brute("test")
        hash = brute.hash("test")
        self.assertNotEqual(hash, "test")
    
    def test_hash_empty_string(self):
        brute = Brute("")
        hash = brute.hash("")
        self.assertEqual(hash, "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e")

    def test_hash_not_string(self):
        with self.assertRaises(TypeError):
            brute = Brute("test")
            brute.hash(123)

    def test_brute_once_normal(self):
        brute = Brute("test")
        attempt = brute.bruteOnce("test")
        self.assertEqual(attempt, True)

    def test_brute_once_wrong_string(self):
        brute = Brute("test")
        attempt = brute.bruteOnce("not test")
        self.assertEqual(attempt, False)


def describe_test_brute_many():
    def describe_random_guess():
        def it_calls_random(mocker):
            ran = mocker.patch.object(random, "randint")
            brute = Brute("test")
            brute.randomGuess()
            ran.assert_called_once()
        


        
    def describe_brute_many():
        def it_calls_brute_once(mocker):
            brute = Brute("test")
            bruteMany = mocker.patch.object(Brute, "bruteOnce")
            brute.bruteMany(1)
            bruteMany.assert_called_once()
    
        def it_returns_the_time(mocker):
            time_mock = mocker.patch.object(time, "time", return_value=1)
            random_mock = mocker.patch.object(Brute, "randomGuess", return_value="test")
            bruteMany = mocker.patch.object(Brute, "bruteOnce")
            b = Brute("test")
            result = b.bruteMany(1)
            assert result == 0

        def it_returns_negative_one(mocker):
            time_mock = mocker.patch.object(time, "time", return_value=1)
            random_mock = mocker.patch.object(Brute, "randomGuess", return_value="test")
            bruteMany = mocker.patch.object(Brute, "bruteOnce", return_value=False)
            b = Brute("test")
            result = b.bruteMany(1)
            assert result == -1