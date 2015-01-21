#define CATCH_CONFIG_MAIN

#include "catch.hpp"
#include "demolib.h"

TEST_CASE( "Sums are computed", "[sum]" ) {
    REQUIRE( sum(1, 2) == 3 );
    REQUIRE( sum(-1, 1) == 0 );
    REQUIRE( sum(0, 0) == 0 );
}
