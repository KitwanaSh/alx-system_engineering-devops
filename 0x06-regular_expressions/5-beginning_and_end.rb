#!/usr/bin/env ruby
# This script only accepts word that starts with h and ends with n

puts ARGV[0].scan(/^h.n$/).join