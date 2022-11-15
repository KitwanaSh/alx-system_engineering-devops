#!/usr/bin/env ruby
# This script is about a regular expression
# That only accepts cpital letters

puts ARGV[0].scan(/[A-Z]/).join
