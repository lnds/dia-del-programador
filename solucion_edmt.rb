#!/usr/bin/env ruby

def challenge year
  now                      = Time.now
  current_year             = now.year
  this_year_programmer_day = programmer_day year

  case
    when year < 2002          then not_yet
    when year < 2009          then russian_only
    when year <  current_year then past year
    when year == current_year && now.yday > this_year_programmer_day.yday  then past year
    when year == current_year && now.yday == this_year_programmer_day.yday then today
    when year == current_year && now.yday < this_year_programmer_day.yday  then future year
    when year >  current_year then future year
  end
end

def programmer_day year, programmer_day = 256, seconds_in_a_day = 60 * 60 * 24
  Time.new(year, 1, 1) + (programmer_day - 1) * seconds_in_a_day
end

def programmer_day_details programmer_day
  day                      = programmer_day.day
  week_day_name            = format_day programmer_day.wday
  month_name               = format_month programmer_day.month
  [day, week_day_name, month_name]
end

def not_yet
  'Aún no se celebra el día del programador'
end

def russian_only
  'Здравствуйте'
end

def past year
  day, week_day_name, month_name = programmer_day_details programmer_day year
  "El día del programador del año #{year} se celebró el #{week_day_name} #{day} de #{month_name}"
end

def future year
  day, week_day_name, month_name = programmer_day_details programmer_day year
  "El día del programador del año #{year} se celebrará el #{week_day_name} #{day} de #{month_name}"
end

def today
  '¡El día del programador se celebra hoy! ¡Felicidades!'
end

def format_day day
  {
    0 => 'domingo',
    1 => 'lunes',
    2 => 'martes',
    3 => 'miércoles',
    4 => 'jueves',
    5 => 'viernes',
    6 => 'sábado'
  }.fetch day
end

def format_month month
  {
    0  => 'enero',
    1  => 'febrero',
    2  => 'marzo',
    3  => 'abril',
    4  => 'mayo',
    5  => 'junio',
    6  => 'julio',
    7  => 'agosto',
    8  => 'septiembre',
    9  => 'octubre',
    10 => 'noviembre',
    11 => 'diciembre'
  }.fetch month - 1
end

puts challenge ARGV[0].to_i
