#!/usr/bin/perl

# 1.  Write a Perl function that takes in a password and checks whether it's valid.  The password should follow the following rule:

#     Passwords must be at least 8 characters long.
#     Between 8-11: requires mixed case letters, numbers and symbols
#     Between 12-15: requires mixed case letters and numbers
#     Between 16-19: requires mixed case letters
#     20+: any characters desired

# You can test out any passwords here
$password = '1234567890123456a@A';

# This runs the check_password function with the argument above
check_password($password);

# main check password function
sub check_password{
    $str = $_[0];
    $len = length($str);
    # if length is less than 8, then it's invalid
    if($len < 8) {
        print "Invalid";
    } elsif($len < 12) { # if length is less than 12, then the mixed case, numbers, and symbols tests are ran
        if ($str =~ /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9])/) {
            print "Valid";
        } else {
            print "Invalid";
        }
    } elsif($len < 16){ # if length is less than 16, then mixed case and numbers tests are ran
        if ($str =~ /(?=.*?[a-z])(?=.*?[A-Z])(?=.*[0-9])/) {
            print "Valid";
        } else {
            print "Invalid";
        }
    } elsif($len < 20){ # if length is less than 20, then only mixed case test is ran
        if ($str =~ /(?=.*?[a-z])(?=.*?[A-Z])/) {
            print "Valid";
        } else {
            print "Invalid";
        }
    }
    else{ #if length is 20 and greater, then it's automatically valid
        print "Valid"
    } 
}

# symbol test
# sub check_symbol {
#     $str = $_[0];
#     if ($str =~ /[^a-zA-z0-9]/) {
#         return 1;
#     } else {
#         return 0;
#     }
# }

# mixed case test
# sub check_mixed_case {
#     $str = $_[0];
#     if ($str =~ /[a-z]/ && $str =~ /[A-Z]/) {
#         return 1;
#     } else {
#         return 0;
#     }
# }

# numbers test
# sub check_numbers {
#     $str = $_[0];
#     if ($str =~ /[0-9]/) {
#         return 1;
#     } else {
#         return 0;
#     }
# }

