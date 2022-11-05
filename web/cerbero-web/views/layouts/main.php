<?php

/* @var $this \yii\web\View */
/* @var $content string */

use yii\helpers\Html;

\hail812\adminlte3\assets\FontAwesomeAsset::register($this);
\hail812\adminlte3\assets\AdminLteAsset::register($this);
$this->registerCssFile('https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback');

$assetDir = Yii::$app->assetManager->getPublishedUrl('@vendor/almasaeed2010/adminlte/dist');

$publishedRes = Yii::$app->assetManager->publish('@vendor/hail812/yii2-adminlte3/src/web/js');
$this->registerJsFile($publishedRes[1] . '/control_sidebar.js', ['depends' => '\hail812\adminlte3\assets\AdminLteAsset']);
?>
<?php $this->beginPage() ?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="<?= Yii::$app->charset ?>">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php $this->registerCsrfMetaTags() ?>
    <title><?= Html::encode($this->title) ?></title>
    <?php $this->head() ?>
</head>


<body class="hold-transition sidebar-mini">
    <?php
    $this->beginBody() ?>

    <div class="wrapper">
        <?php if (!Yii::$app->user->isGuest) { ?>
            <?= $this->render('navbar', ['assetDir' => $assetDir]) ?>
            <?= $this->render('sidebar', ['assetDir' => $assetDir]) ?>
        <?php } ?>
  
        <?= $this->render('content', ['content' => $content, 'assetDir' => $assetDir]) ?>
        
        <?php if (!Yii::$app->user->isGuest) { ?>
            <?= $this->render('control-sidebar') ?>
            <?= $this->render('footer') ?>
        <?php } ?>
    </div>

    <?php $this->endBody() ?>
</body>

</html>
<?php $this->endPage() ?>