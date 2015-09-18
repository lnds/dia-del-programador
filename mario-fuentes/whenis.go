/* DISCLAIMER: this is my first experiment in GO, apologies for any mistake.
 * RESOLVE: http://www.lnds.net/blog/lnds/2015/9/13/feliz-dia-de-los-programadores
 * 
 * Released under the terms of the MIT License
 * Copyright (c) 2015 https://github.com/mario-fuentes/dia-del-programador
 *
 * Usage: go run whenis.go -year YYYY
 */
package main

import (
	"flag"
	"fmt"
	"time"
)

func main() {
	const (
		programmerDayCreation = 2002
		programmerDayGlobalAdoption = 2009
		programmerDayOfYear = 256
		outputFormatEs = "El día del programador del año %d se celebr%s el %s %d de %s\n"
		outputFormatPastRu = "День разработчика %d состоялось в %s, %d %s\n"
	)
	
	// time.Format(...) is just printing in English, and time.LoadLocation(...) isn't
	// changed the weekdays and months words to the specified language, so let go by hands...   
	var weekdaysEs = [...]string {"Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"}
	var monthsEs = [...]string {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"}
	var weekdaysRu = [...]string {"Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"}
	var monthsRu = [...]string {"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"}
	
	year := flag.Int("year", 0, "El parámetro 'year' corresponde al año en formato YYYY mayor que zero para determinar la fecha del Dia del Programador.")
	
	if flag.Parse(); *year < programmerDayCreation {
		if fmt.Println("El día del programador solo fue instaurado el año 2002"); *year <= 0 {
			 flag.PrintDefaults();
		}
		return;
	}
	
	progDay := time.Date(*year, time.January, 1, 0, 0, 0, 0, time.UTC).AddDate(0, 0, programmerDayOfYear - 1)
	now := time.Now()
	today := time.Date(now.Year(), now.Month(), now.Day(), 0, 0, 0, 0, time.UTC);
	
	switch {
		case !progDay.Before(today) && !progDay.After(today):
			fmt.Println("El día del programador se celebra hoy! Felicidades!")
		case *year >= programmerDayCreation && *year < programmerDayGlobalAdoption:
			fmt.Printf(outputFormatPastRu, *year, weekdaysRu[progDay.Weekday()], progDay.Day(), monthsRu[int(progDay.Month()) - 1])
		default:
			var suffix string
			if suffix = "ó"; progDay.After(today) { suffix = "ará" }
			fmt.Printf(outputFormatEs, *year, suffix, weekdaysEs[progDay.Weekday()], progDay.Day(), monthsEs[int(progDay.Month()) - 1])
	}
}
