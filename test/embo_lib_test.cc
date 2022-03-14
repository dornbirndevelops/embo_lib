#include <embo_lib.hh>
#include <gtest/gtest.h>

TEST(EmboLibTest, HasGreeting) {
    const std::string actual = embo_lib::greeting();
    EXPECT_FALSE(actual.empty());
}

TEST(EmboLibTest, CorrectGreeting) {
    const std::string actual = embo_lib::greeting();
    EXPECT_EQ(actual, "Hello embo++!");
}
