<?php

use yii\helpers\Html;
use yii\widgets\DetailView;

/** @var yii\web\View $this */
/** @var app\models\Veiculo $model */

$this->title = 'Placa ' . $model->placa;
$this->params['breadcrumbs'][] = ['label' => 'Veiculos', 'url' => ['index']];
$this->params['breadcrumbs'][] = $this->title;
\yii\web\YiiAsset::register($this);
?>
<div class="veiculo-view card card-outline card-primary">

    <div class="card-header">
        <h1><?= Html::encode($this->title) ?></h1>
    </div>

    <div class="card-body">
        <?= DetailView::widget([
            'model' => $model,
            'attributes' => [
                //'id',
                'placa:ntext',
                'data',
                [
                    'attribute' => 'imagem',
                    'value' => 'data:image/jpg;base64,' . $model->imagem,
                    'format' => ['image', ['width' => '100%', 'height' => '100%']]
                ],
               
            ],
        ]) ?>

    </div>

</div>