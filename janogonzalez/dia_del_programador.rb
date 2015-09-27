#!/usr/bin/env ruby
# encoding: UTF-8

require 'date'

PROGRAMMERS_DAY_NUMBER = 256
DAYS_ES = %w(domingo lunes martes miércoles jueves viernes sábado)
MONTHS_ES = %w(enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre)

def programmers_day(year)
  Date.ordinal(year, PROGRAMMERS_DAY_NUMBER)
end

def to_es_str(date)
  "#{DAYS_ES[date.wday]} #{date.day} #{MONTHS_ES[date.month - 1]}"
end

def result(year)
  today = Date.today

  if year < 2002
    "En esta fecha no se celebraba el día del programador"
  elsif year < 2009
    "Он по-прежнему отмечается программист"
  elsif today.year > year || (today.year == year && today.yday > PROGRAMMERS_DAY_NUMBER)
    "El día del programador del año #{year} se celebró el #{to_es_str(programmers_day(year))}"
  elsif today.year == year && today.yday == PROGRAMMERS_DAY_NUMBER
    "El día del programador se celebra hoy! Felicidades!"
  else
    "El día del programador del año #{year} se celebrará el #{to_es_str(programmers_day(year))}" 
  end
end

year = Integer(ARGV[0])
puts result(year)
