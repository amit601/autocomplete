#!/usr/bin/env ruby


require 'rubygems'
require 'redis'

r = Redis.new

n = ARGV.to_s
n.strip!
(3...(n.length-2)).each{|l|
    prefix = n[2...l]
    puts prefix
    r.zadd(:redisdb,0,prefix)
}
nf=n[2...n.length-2]+"*"
puts nf
r.zadd(:redisdb,0,nf)

