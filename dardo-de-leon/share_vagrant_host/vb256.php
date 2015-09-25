<?php 
/**
 * El Día de los Programadores.
 * Propuesto por Valentin Balt, se celebra el 256º día de cada año.
 * @link https://es.wikipedia.org/wiki/D%C3%ADa_de_los_Programadores 
 *
 * @author Dardo De León
 */
$inicoCelebracion = 2002;
$seCelebraEnRusia = 2009;
$diaDeCelebracion = pow(2, 8);

$resultado = 'El programa requiere recibir como argumento el año(-a YYYY) del cual se quiere saber la fecha en que se celebro o celebrará el día del programador';

$parametros = getopt('a:');
if (isset($parametros['a']) && strlen(preg_replace('/^[0-9]{1,4}/', '', $parametros['a']))===0) {
    $anio = (int) $parametros['a'];
    if ($anio >= $inicoCelebracion) {
        /**
         * En este punto podría realizarse la asignación del nuevo valor a $diaDeCelebracion sin afectar las respuestas
         * de los años pasados donde el día de celebración era el número 256 del año; solo admite un cambio de fecha :)
         * $diaDeCelebracion = ($anio >= $anioEnQueCambioElDiaDeCelebracion) ? $nuevoDiaDeCelebracion : $diaDeCelebracion;
         */
        $dia = new DateTime(vsprintf('%d-01-01 00:00:00', $anio));
        $dia->add(new DateInterval(vsprintf('P%dD', $diaDeCelebracion-1)));
        $hoy = new DateTime(date('Y-m-d 00:00:00'));
        if ($dia != $hoy) {
            if ($anio < $seCelebraEnRusia) {
                setlocale(LC_ALL, 'ru_RU.UTF-8');
                $resultado = 'День разработчика в %d году был проведен в %s, %d %s';
            } else {
                setlocale(LC_ALL, 'es_ES.UTF-8');
                $resultado = ($dia > $hoy) 
                    ? 'El día del programador del año %d se celebrará el %s %d de %s' 
                    : 'El día del programador en %d se celebró el %s %d de %s';
            }
            $resultado = vsprintf($resultado, [$anio, strftime('%A', $dia->getTimestamp()), $dia->format('d'), strftime('%B', $dia->getTimestamp())]);
        } else {
            $resultado = 'El día del programador se celebra hoy! Felicidades!';
        }
    } else {
        $resultado = vsprintf('En el año %d aún no se celebraba el día del programador', $anio);
    }    
}
echo $resultado . PHP_EOL;