<?php

use app\models\Usuarios;
use yii\helpers\Html;
use yii\helpers\Url;
use yii\grid\ActionColumn;
use yii\grid\GridView;

/** @var yii\web\View $this */
/** @var app\models\UsuariosSearch $searchModel */
/** @var yii\data\ActiveDataProvider $dataProvider */

$this->title = 'Usuarios';
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="usuarios-index card card-outline card-primary">

    <div class="card-header">
            <?= Html::a('Adicionar Usuário', ['create'], ['class' => 'btn btn-primary']) ?>
    </div>

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
                'nome:ntext',
                'usuario:ntext',
                //'senha:ntext',
                [
                    'class' => ActionColumn::className(),
                    'urlCreator' => function ($action, Usuarios $model, $key, $index, $column) {
                        return Url::toRoute([$action, 'id' => $model->id]);
                    }
                ],
            ],
        ]); ?>
    </div>

</div>