#!/usr/bin/env ruby
# The regex that matches 10 digit phone number

puts ARGV[0].scan(/^\d{10,10}$/).join
