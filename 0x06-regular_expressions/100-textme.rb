#!/usr/bin/env ruby
puts ARGV[0].scan(/[A-Z0-9+?\[?\]?]*,?[ -]?/).join
