
import pytest

from car_insurance_premium import (
    annual_premium,
    no_claim_bonus,
    claim_payout
)


# ANNUAL PREMIUM TEST CASES

def test_invalid_car_type():
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 1, False)


def test_driver_below_18():
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 1, False)


def test_young_driver():
    assert annual_premium("hatchback", 20, 1, False) == 12000


def test_middle_age_driver():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_senior_driver():
    assert annual_premium("suv", 60, 1, False) == 17000


def test_zero_claims():
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_one_claim():
    assert annual_premium("sedan", 30, 1, False) == 12000


def test_more_than_two_claims():
    assert annual_premium("hatchback", 30, 3, False) == 16000


def test_anti_theft_true():
    assert annual_premium("sedan", 30, 1, True) == 11500


def test_anti_theft_false():
    assert annual_premium("sedan", 30, 1, False) == 12000


# NO CLAIM BONUS TEST CASES

def test_negative_claim_free_years():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


def test_zero_claim_free_years():
    assert no_claim_bonus(0) == 0


def test_one_claim_free_year():
    assert no_claim_bonus(1) == 20


def test_two_claim_free_years():
    assert no_claim_bonus(2) == 20


def test_three_claim_free_years():
    assert no_claim_bonus(3) == 35


def test_four_claim_free_years():
    assert no_claim_bonus(4) == 35


def test_five_claim_free_years():
    assert no_claim_bonus(5) == 50


# CLAIM PAYOUT TEST CASES

def test_negative_damage_cost():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_negative_deductible():
    with pytest.raises(ValueError):
        claim_payout(10000, 50000, -1000, False)


def test_total_loss():
    assert claim_payout(50000, 40000, 1000, True) == 40000


def test_normal_claim():
    assert claim_payout(10000, 50000, 1000, False) == 9000


def test_damage_below_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_damage_equal_to_deductible():
    assert claim_payout(1000, 50000, 1000, False) == 0


def test_payout_exceeds_insured_value():
    assert claim_payout(60000, 40000, 1000, False) == 40000


def test_payout_within_insured_value():
    assert claim_payout(10000, 50000, 1000, False) == 9000
