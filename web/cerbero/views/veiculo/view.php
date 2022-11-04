<?php

use yii\helpers\Html;
use yii\widgets\DetailView;

/* @var $this yii\web\View */
/* @var $model app\models\Veiculo */

$this->title = 'Placa ' . $model->placa;
$this->params['breadcrumbs'][] = ['label' => 'Veiculos', 'url' => ['index']];
$this->params['breadcrumbs'][] = $this->title;
\yii\web\YiiAsset::register($this);
?>

<div class="container-fluid">
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-md-12">
                    <?= DetailView::widget([
                        'model' => $model,
                        'attributes' => [
                            'placa:ntext',
                            'data',
                            [
                                'attribute' => 'imagem',
                                'value' => function ($model) {
                                    $bin = base64_decode($model->imagem);
                                    //return Html::img($bin, ['width' => '100px']);
                                }
                            ],
                            //'imagem:ntext',
                        ],
                    ]) ?>
                </div>
            </div>
        </div>
    </div>
</div>