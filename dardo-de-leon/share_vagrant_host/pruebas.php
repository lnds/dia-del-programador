<?php 
/**
 * Verifica que la versión PHP sea >= 5.6.13
 */
echo 'La versión de PHP es >= 5.6.13: ';
echo version_compare(PHP_VERSION, '5.6.13') >= 0 ? 'OK' : 'ERROR';
echo PHP_EOL.PHP_EOL;

/**
 * Verifica que estén disponibles los "locale" de es_ES y ru_RU
 */
$localismos = ['ru_RU.UTF-8', 'es_ES.UTF-8'];
foreach ($localismos as $local) {
	echo sprintf('Disponibilidad del localismo %s: %s', $local, is_string(setlocale(LC_ALL, $local)) ? 'OK' : 'ERROR');
	echo PHP_EOL;
}
echo PHP_EOL;

/**
 * Presenta la timezone activa y el día/hora actuales
 */
echo sprintf('La timezone activa es "%s" y en este momento señala que es %s', date_default_timezone_get(), (new DateTime(null))->format('d-m-Y H:i:s'));
echo PHP_EOL.PHP_EOL;

/**
 * Verifica la existencia del script que se verificara
 */
$rutina = __DIR__ . DIRECTORY_SEPARATOR .'vb256.php';
if (is_file($rutina) == false) {
	exit(sprintf('El script "%s" no está disponible.', $rutina));
}

/**
 * Ejecuta el programa con una serie de entradas
 */
$parametros = array_merge(['', 'texto', -1, 0], range(2000, 2020, 1), [10000]);
foreach ($parametros as $prueba => $parametros) {
	echo sprintf('Prueba %d: parámetro "%s"%s%s', $prueba+1, $parametros, PHP_EOL, exec('php '. $rutina .' -a '. $parametros));
	echo PHP_EOL.PHP_EOL;
}