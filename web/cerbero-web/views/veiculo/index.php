<?php
use yii\grid\GridView;

/** @var yii\web\View $this */
/** @var app\models\VeiculoSearch $searchModel */
/** @var yii\data\ActiveDataProvider $dataProvider */

$this->title = 'Veiculos';
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="veiculo-index card card-outline card-primary">

    <?php // echo $this->render('_search', ['model' => $searchModel]); 
    ?>

    <div class="card-body">
        <?= GridView::widget([
            'dataProvider' => $dataProvider,
            'filterModel' => $searchModel,
            'summary' => false,
            'columns' => [
                //['class' => 'yii\grid\SerialColumn'],

                //'id',
                'placa:ntext',
                'data',
                [
                    'class' => 'yii\grid\ActionColumn',
                    'template' => '{view}',
                ],
            ],
        ]); ?>
    </div>



</div>